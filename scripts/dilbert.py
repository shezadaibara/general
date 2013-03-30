from pyquery import PyQuery
import urllib
from datetime import date, datetime, timedelta
import os
import zipfile
import shutil


class DilbertScrapper(object):
    
    _input_date_format = '%d-%m-%Y'
    _domain_date_format = '%Y-%m-%d'
    _save_date_format = '%d_%m_%Y'
    _domain_name = 'http://dilbert.com'
    _domain_path = 'strips/comic'
    
    _save_dir = '../dilbert'
    _curr_year = ''
    _curr_month = ''
    
    current_date = ''
    
    def __init__(self, start_date, end_date=None):
        '''
            expected date format is %d-%m-%Y (i.e dd-mm-yyyy)
            example : 16-04-1989
        '''
        try:
            if end_date:
                self.end_date = datetime.strptime(end_date,
                                                  self._input_date_format).date()
            
            self.current_date = datetime.strptime(start_date,
                                                  self._input_date_format).date()
        except ValueError:
            print "ERROR: Expected Date format is incorrect, write your dates as dd-mm-yyyy"
            
    def _get_url(self):
        return '/'.join([self._domain_name,
                        self._domain_path,
                        self.current_date.strftime(self._domain_date_format)])
    
    def scrapper(self):
        while self.current_date <= date.today():
            try:
                url = self._get_url()
                html = PyQuery(url=url)
                image = html('div').filter('.STR_Image').find('img')
                
                source = self._get_image_source_url(image.attr('src'))
                destination = self._get_image_destination_path()
                
                self.download(source, destination)
                
            except Exception as e:
                tmp = self.current_date.strftime(self._input_date_format)
                print '{}:{}'.format(type(e), str(e))
                print 'comic {} skipped'.format(tmp)
            
            self.current_date += timedelta(days=1)
            if self.current_date == self.end_date:
                print 'task completed'
                break
    
    def _get_image_source_url(self, img_src):
        return '/'.join([self._domain_name, img_src])
    
    def _get_image_destination_path(self):
        
        if not os.path.exists(self._save_dir):
            os.makedirs(self._save_dir)
        
        if any([self._curr_month != str(self.current_date.month),
                self._curr_year != str(self.current_date.year)]):
            
            if self._curr_month != '':
                self._zip_directory()
            
            self._curr_year = str(self.current_date.year)
            self._curr_month = str(self.current_date.month)
            print str(self.current_date)
            os.makedirs('/'.join([self._save_dir, self._curr_year, self._curr_month]))
            
        return '/'.join([self._save_dir,
                         self._curr_year,
                         self._curr_month,
                         self.current_date.strftime(self._save_date_format)]
                        ) + '.jpg'
    
    def download(self, source, destination):
        urllib.urlretrieve(source, destination)
        
    def _zip_directory(self):
        target_dir = '/'.join([self._save_dir,
                         self._curr_year,
                         self._curr_month]
                        )
        
        zfp = zipfile.ZipFile('{}.zip'.format(target_dir), 'w', zipfile.ZIP_DEFLATED)
        
        rootlen = len(target_dir) + 1
        
        for base, _dirs, files in os.walk(target_dir):
            for _file in files:
                fn = os.path.join(base, _file)
                zfp.write(fn, fn[rootlen:])
        
        #deleting the target directory because after zip why do you require the original directory
        shutil.rmtree(target_dir)
        

if __name__ == '__main__':
    DilbertScrapper('30-01-2012', '2-02-2012').scrapper()
